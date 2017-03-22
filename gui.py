from collections import OrderedDict

import units
import tkinter
from fractions import Fraction


def textvariable(master, default='', callback=None):
    variable = tkinter.StringVar(master)
    variable.set(default)
    if callback:
        variable.trace('w', lambda name, index, mode, sv=variable: callback(sv.get()))
    return variable


def pull_down_menu(master, options, default=None, callback=None, **kwargs):
    if default is None:
        default = options[0]
    variable = textvariable(master, default, callback)
    r = tkinter.OptionMenu(master, variable, *options, **kwargs)
    r.textvariable = variable
    return r


def update_pdm(pdm, options, default=None):
    if default is None:
        default = options[0]
    pdm['menu'].delete(0, 'end')
    for o in options:
        pdm['menu'].add_command(label=o, command=tkinter._setit(pdm.textvariable, o))
    # pdm.textvariable.set(default)
    pdm.after(1, lambda: pdm.textvariable.set(default))


class Application(tkinter.Frame):
    def __init__(self, master=None):
        master.title("Converter")
        super(Application, self).__init__(master=master)
        self.value_types = OrderedDict(((t.__name__, t) for t in units.value_types))
        self.prefixes = OrderedDict(((p.display_name, p) for p in units.prefixes))
        self.units = OrderedDict(((u.display_name, u) for u in units.units))
        self.units_vt = {t.__name__: [u.display_name for u in t.units] for t in units.value_types}
        self.pack()

        # UI: 12 columns (0-11)
        self.title = tkinter.Label(self, text='Converter')
        self.title.grid(row=0, column=3, columnspan=6)

        self.value_type_label = tkinter.Label(self, text='Type')
        self.value_type_label.grid(row=1, column=5)
        self.value_type = pull_down_menu(self, list(self.value_types.keys()), callback=self.on_change_type)
        self.value_type.grid(row=1, column=6)

        self.data_in = tkinter.Entry(self, textvariable=textvariable(self, '0', self.on_change_data))
        self.data_in.grid(row=2, column=0, columnspan=3)
        self.prefix_in = pull_down_menu(self, list(self.prefixes.keys()), '-', callback=self.on_change_data)
        self.prefix_in.grid(row=2, column=3)
        self.unit_in = pull_down_menu(self, list(self.units.keys()), callback=self.on_change_data)
        self.unit_in.grid(row=2, column=4)

        self.btn_switch = tkinter.Button(self, text='<-Switch->', command=self.on_switch)
        self.btn_switch.grid(row=2, column=5, columnspan=2)

        self.data_out = tkinter.Entry(self, {}, textvariable=textvariable(self, '0', self.on_change_data))
        self.data_out.grid(row=2, column=7, columnspan=3)
        self.prefix_out = pull_down_menu(self, list(self.prefixes.keys()), '-', callback=self.on_change_data)
        self.prefix_out.grid(row=2, column=10)
        self.unit_out = pull_down_menu(self, list(self.units.keys()), callback=self.on_change_data)
        self.unit_out.grid(row=2, column=11)

        self.quit_btn = tkinter.Button(self, text='Quit', command=self.quit)
        self.quit_btn.grid(row=3, column=5, columnspan=2)

        self.about = tkinter.Label(self, text='By Szymon Zmilczak & Adrian Ćwiertnia')
        self.about.grid(row=4, column=7, columnspan=6)

        self.on_change_type(self.value_type.textvariable.get())

    def on_switch(self):
        u_in = self.unit_in.textvariable.get()
        p_in = self.prefix_in.textvariable.get()
        u_out = self.unit_out.textvariable.get()
        p_out = self.prefix_out.textvariable.get()
        v_out = self.data_out.get()

        self.unit_out.textvariable.set(u_in)
        self.prefix_out.textvariable.set(p_in)
        self.unit_in.textvariable.set(u_out)
        self.prefix_in.textvariable.set(p_out)
        self.data_in.delete(0, 'end')
        self.data_in.insert(0, v_out)

        self.on_change_data(None)

    def on_change_type(self, data):
        update_pdm(self.unit_in, self.units_vt[data])
        update_pdm(self.unit_out, self.units_vt[data])
        self.on_change_data(None)

    # def on_in_error(self):
    #     self.data_in['bg'] = 'red'

    def on_change_data(self, *args):
        try:
            v_in = Fraction(self.data_in.get().replace(',', '.'))
        except ValueError:
            self.data_in['bg'] = 'red'
            # self.data_in.after(2, lambda: self.on_in_error())
            return
        self.data_in['bg'] = 'white'
        u_in = self.unit_in.textvariable.get()
        p_in = self.prefix_in.textvariable.get()
        u_out = self.unit_out.textvariable.get()
        p_out = self.prefix_out.textvariable.get()
        U_in = self.units[u_in]
        P_in = self.prefixes[p_in]
        U_out = self.units[u_out]
        P_out = self.prefixes[p_out]
        IN = P_in(U_in)
        OUT = P_out(U_out)
        if IN.value_type.compatible_with(OUT.value_type):
            V_out = IN(v_in).convert_to(OUT)
            v_out = V_out.smart_str(20)
            self.data_out.delete(0, 'end')
            self.data_out.insert(0, v_out)


def main():
    root = tkinter.Tk()
    app = Application(master=root)
    app.mainloop()
    try:
        root.destroy()
    except tkinter.TclError:
        pass


if __name__ == '__main__':
    main()

