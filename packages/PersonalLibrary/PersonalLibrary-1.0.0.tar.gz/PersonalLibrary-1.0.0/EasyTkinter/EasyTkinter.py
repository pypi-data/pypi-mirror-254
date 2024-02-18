from functools import wraps
from typing import Any, Self

from tkinter import *

try:
    from Controllers import Controllers
except ImportError:
    from EasyTkinter.Controllers import Controllers

from Initial import Logger
from Text.Text import Text


class EasyTkinter:
    def __init__(self, title: str = 'tkinter GUI', size: tuple = (800, 600),
                 resizable: tuple[bool] = (False, False)) -> None:
        Logger.info('EasyTkinter')
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{size[0]}x{size[1]}")
        self.root.resizable(resizable[0], resizable[1])

        self.menuDict = dict()
        self.labelDict = dict()
        self.textDict = dict()
        self.buttonDict = dict()
        self.entryDict = dict()
        self.canvasDict = dict()
        self.labelFrameDict = dict()
        self.checkbuttonDict = dict()
        self.radiobuttonDict = dict()

        self.supportController: dict = {
            "label": self.labelDict,
            "text": self.textDict,
            "button": self.buttonDict,
            "label_frame": self.labelFrameDict,
            "entry": self.entryDict,
            "checkbutton": self.checkbuttonDict,
            "radiobutton": self.radiobuttonDict,
            "menu": self.menuDict
        }

        self.Controller: dict = {
            "label": Label,
            "text": Text,
            "button": Button,
            "label_frame": LabelFrame,
            "entry": Entry,
            "checkbutton": Checkbutton,
            "radiobutton": Radiobutton,
            "menu": Menu
        }

        self.controllerFuncDict: dict = dict()

    def getRoot(self) -> Tk:
        return self.root

    @Logger.ShowLog
    def start(self, n: int = 0) -> None:
        Logger.info(Text().translate("info.tkinter.show"))
        self.root.mainloop(n)

    def stop(self) -> None:
        self.root.quit()

    def destroy(self) -> None:
        self.root.destroy()

    def show(self) -> None:
        self.root.deiconify()

    def hide(self) -> None:
        self.root.withdraw()

    def setIcon(self, path: str) -> None:
        self.root.iconbitmap(path)

    @Logger.ShowLog
    def BuildController(self,
                        controllerName: str,
                        controller: Controllers | str,
                        master: Tk | Toplevel | LabelFrame = None,
                        **options) -> Self:
        if master is None:
            master = self.root
        if controller not in self.supportController:
            Logger.error(
                Text().translate("error.tkinter.controller_not_supported").formatted(controller,
                                                                                     list(self.supportController.keys())
                                                                                     )
            )
        if not self._matchControllerName(controllerName):
            self.supportController[controller][controllerName] = self.Controller[controller](master, **options)
        else:
            Logger.error(
                Text().translate("error.tkinter.controller_already_exist").formatted(controllerName, controller))
        return self

    def getController(self, controllerName: str, controller: Controllers | str) -> Any:
        try:
            return self.supportController[controller][controllerName]
        except KeyError:
            return None

    def SetControllerGrid(self, controllerName: str, controller: Controllers | str, row: int, column: int,
                          **gridOptions) -> None:
        self.getController(controllerName, controller).grid(row=row, column=column, **gridOptions)

    def SetControllerPack(self, controllerName: str, controller: Controllers | str, **packOptions) -> None:
        self.getController(controllerName, controller).pack(**packOptions)

    def controllerFunction(self, controllerName: str, controller: Controllers | str, *args, **kwargs):
        """
        装饰器，用于可调用按钮的添加
        :param controller: 控件
        :param controllerName: 控件名称
        :return:
        """

        def decorator(func):
            self.controllerFuncDict[controllerName] = func

            @wraps(func)
            def wrapper(*TArgs, **TKwargs):
                if self._matchControllerName(controllerName):
                    self.supportController[controller][controllerName].config(
                        command=lambda: self.controllerFuncDict[controllerName](*TArgs, **TKwargs))
                else:
                    Logger.error(
                        Text().translate("error.tkinter.controller_not_build").formatted(controllerName, controller))

            wrapper(*args, **kwargs)
            return wrapper

        return decorator

    def _matchControllerName(self, controllerName: str):
        tmpDict = {}
        for controller in self.supportController.values():
            tmpDict.update(controller)
        return controllerName in tmpDict


if __name__ == "__main__":
    easyTkinter = EasyTkinter()
    easyTkinter.BuildController("testLabel", "label", text="label").SetControllerGrid("testLabel", Controllers.LABEL,
                                                                                      row=1,
                                                                                      column=1)
    easyTkinter.BuildController("testButton", "button", text="button", width=10).SetControllerGrid("testButton",
                                                                                                   Controllers.BUTTON,
                                                                                                   row=2,
                                                                                                   column=1)


    @easyTkinter.controllerFunction("testButton", "button")
    def Hello(name):
        Logger.info(f"Hello World!" + name)


    easyTkinter.start()
