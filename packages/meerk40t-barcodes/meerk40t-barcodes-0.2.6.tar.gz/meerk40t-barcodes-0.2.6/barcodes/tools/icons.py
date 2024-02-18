import threading

STD_ICON_SIZE = 50

def barcode_icon():
    try:
        from meerk40t.gui.icons import VectorIcon
        vector_icon = VectorIcon(
            stroke=(),
            fill=(
                "M8,7h7V42H8ZM18.5,7H22V42H18.5Zm7,0H29V42H25.5ZM36,7h3.5V42H36ZM50,7h3.5V42H50ZM60.5,7H64V42H60.5ZM43,7h1.75V42H43ZM32.5,7h1.75V42H32.5ZM55.25,7H57V42H55.25ZM8,45.5h3.5V49H8Zm10.5,0H22V49H18.5Zm7,0H29V49H25.5Zm17.5,0h3.5V49H43Zm17.5,0H64V49H60.5ZM50,45.5h7V49H50Zm-17.5,0h7V49h-7V45.5Z",
            ),
        )
        return vector_icon
    except (ImportError, AttributeError):
        from meerk40t.gui.icons import PyEmbeddedImage
        bitmap_icon = PyEmbeddedImage(
            b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAA'
            b'4ElEQVRoge3Zuw3CMBSF4R9EzwIwAQswAgtkAjaABVgAqNLBBmnooKOkShcWSJmKCaBxkGXZ'
            b'RkIUF+l8kmX5+nlqg4iIyPcGkdoOmHrjLXADlsAic1YDbIAJsA/mCtcfgHFkb+qOM3AE5sDa'
            b'q7fAKvOW94OeXusfUQb1sF3dullkrtcl9qbuKF29COpN+Ojhp1T/QkGsURBrFMQaBbFGQaxR'
            b'EGsUxBoFsUZBrFEQaxTEGgWxRkGsURBrFMSaUaR2Ae7euHV9DVSZs/o/i0dm3Yn4R0/qjtqb'
            b'ryLrRUREfuIFnSA3JAyP8hcAAAAASUVORK5CYII=')
        return bitmap_icon