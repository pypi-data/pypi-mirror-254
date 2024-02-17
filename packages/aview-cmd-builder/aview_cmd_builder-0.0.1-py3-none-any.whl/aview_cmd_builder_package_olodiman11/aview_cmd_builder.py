class CmdBuilder:

    def __init__(self):
        self.commands_separator = "\n"
        self.header_template = "----------------------{0}----------------------"
        self.__cmdArray = []
        self.__command_line_separator = " &\n"
        self.__lines = []

    def import_command(self, path):
        self.__lines.append(f'file command read file="{path}"')
        self.__makeCommand()
        return self

    def display_sim_panel(self):
        self.__lines.append(f'interface dialog display dialog=.gui.sim_int_panel')
        self.__makeCommand()
        return self

    def display_table(self):
        self.__lines.append(f'interface dialog display dialog=.gui.sim_dbg_mon_panel')
        self.__makeCommand()
        return self

    def create_spline(self, name, x, y, units="no_units"):
        self.__lines.append(f"data_element create spline")
        self.__lines.append(f"\tspline_name={CmdBuilder.__escape_special_chars(name)}")
        self.__lines.append(f"\tx={CmdBuilder.__format_array(x)}")
        self.__lines.append(f"\ty={CmdBuilder.__format_array(y)}")
        self.__lines.append(f"\tlinear_extrapolate=no")
        self.__lines.append(f"\tunits={units}")
        self.__lines.append(f"\tcomments=\"\"")
        self.__makeCommand()
        return self

    def modify_spline(self, name, x, y, units="no_units"):
        self.__lines.append(f"data_element modify spline")
        self.__lines.append(f"\tspline={CmdBuilder.__escape_special_chars(name)}")
        self.__lines.append(f"\tx={CmdBuilder.__format_array(x)}")
        self.__lines.append(f"\ty={CmdBuilder.__format_array(y)}")
        self.__lines.append(f"\tlinear_extrapolate=no")
        self.__lines.append(f"\tunits={units}")
        self.__lines.append(f"\tcomments=\"\"")
        self.__makeCommand()
        return self

    def modify_variable(self, name, value, units="no_units"):
        self.__lines.append(f"variable modify")
        self.__lines.append(f"\tvariable_name={CmdBuilder.__escape_special_chars(name)}")
        self.__lines.append(f"\treal={value}")
        self.__lines.append(f"\tdelta_type=relative")
        self.__lines.append(f"\trange=-1.0, 1.0")
        self.__lines.append(f"\tunits={units}")
        self.__lines.append(f"\tuse_range=yes")
        self.__lines.append(f"\tcomments=\"\"")
        self.__makeCommand()
        return self

    def import_data(self, path, time_index=1):
        self.__lines.append(f"file testdata read measures")
        self.__lines.append(f"\tuse_file_column_labels=yes")
        self.__lines.append(f"\tindependent_column_index={time_index}")
        self.__lines.append(f'\tfile_name = "{path}"')
        self.__makeCommand()
        return self

    def save_data(self, path, *args, start=None, end=None):
        self.__lines.append(f"numeric_results write")
        self.__lines.append(f"\tresult_set_component_name={CmdBuilder.__format_array(args)}")
        self.__lines.append(f"\twrite_to_terminal=off")
        self.__lines.append(f"\torder=ascending")
        self.__lines.append(f"\tsort_by=by_time")
        if start is not None:
            self.__lines.append(f"\tabove_value={start}")
        if end is not None:
            self.__lines.append(f"\tbelow_value={end}")
        self.__lines.append(f'\tfile_name="{path}"')
        self.__makeCommand()
        return self

    def run_scripted_simulation(self, name, reset=True):
        reset = "yes" if reset else "no"
        self.__lines.append(f"simulation single scripted")
        self.__lines.append(f"\tsim_script_name={CmdBuilder.__escape_special_chars(name)}")
        self.__lines.append(f"\treset_before_and_after={reset}")
        self.__makeCommand()
        return self

    def modify_script(self, name, code):
        code = ", ".join([f'"{x.strip()}"' for x in code.split('\n') if x.strip()])
        self.__lines.append(f"simulation script modify")
        self.__lines.append(f"\tsolver_commands={code}")
        self.__lines.append(f"\tsim_script_name={name}")
        self.__lines.append(f'\tcomment=""')
        self.__makeCommand()
        return self

    def set_file_prefix(self, prefix):
        self.__lines.append(f'simulation set file_prefix="{prefix}"')
        self.__makeCommand()
        return self

    def set_update_graphics_display(self, flag):
        self.__lines.append(f'.sim_preferences.update={1 if flag else 0}')
        self.__makeCommand()
        return self

    def create_header(self, text):
        self.__cmdArray.append(f"!{self.header_template.format(text)}")
        return self

    def save_cmd(self, path):
        with open(path, "w") as file:
            file.write(f"\n{self.commands_separator}".join(self.__cmdArray))

    def rename_part(self, old_name, new_name):
        self.__lines.append(f'entity modify')
        self.__lines.append(f'\tentity={old_name}')
        self.__lines.append(f'\tnew={new_name}')
        self.__makeCommand()
        return self

    def modify_bushing(self, name, stiffness=(0, 0, 0), damping=(0, 0, 0), preload=(0, 0, 0),
                                  tstiffness=(0, 0, 0), tdamping=(0, 0, 0), tpreload=(0, 0, 0), comments=""):
        self.__lines.append(f'force modify element_like bushing')
        self.__lines.append(f'\tbushing_name={name}')
        self.__lines.append(f'\tstiffness={self.__format_array(stiffness)}')
        self.__lines.append(f'\tdamping={self.__format_array(damping)}')
        self.__lines.append(f'\tforce_preload={self.__format_array(preload)}')
        self.__lines.append(f'\ttstiffness={self.__format_array(tstiffness)}')
        self.__lines.append(f'\ttdamping={self.__format_array(tdamping)}')
        self.__lines.append(f'\ttorque_preload={self.__format_array(tpreload)}')
        self.__lines.append(f'\tcomments="{comments}"')
        self.__makeCommand()

    def modify_inertial_properties(self, name, mass, ixx, iyy, izz, cm='cm'):
        self.__lines.append(f'part modify rigid mass_properties')
        self.__lines.append(f'\tpart_name={name}')
        self.__lines.append(f'\tmass={mass}')
        self.__lines.append(f'\tcenter_of_mass_marker={name}.{cm}')
        self.__lines.append(f'\tixx={ixx}')
        self.__lines.append(f'\tiyy={iyy}')
        self.__lines.append(f'\tizz={izz}')
        self.__makeCommand()

    def modify_marker(self, name, location=None, orientation=None):
        self.__lines.append(f'marker modify')
        self.__lines.append(f'\tmarker_name={name}')
        if location:
            self.__lines.append(f'\tlocation={self.__format_array(location)}')
        if orientation:
            self.__lines.append(f'\torientation={self.__format_array(orientation)}')
        self.__makeCommand()

    @staticmethod
    def __escape_special_chars(string):
        return string\
            .replace("\"", r"\"")\
            .replace("\\", r"\\")

    @staticmethod
    def __format_array(array):
        return ", ".join([str(x) for x in array])

    def __makeCommand(self):
        self.__cmdArray.append(self.__command_line_separator.join(self.__lines))
        self.__lines.clear()

