def compute_Frot(rot, ux, uy, f_radial):
    """Compute cross-product of absolute potential vorticity with velocity."""
    rot_abs = rot + f_radial
    F1x = rot_abs * uy
    F1y = -rot_abs * ux
    return (F1x, F1y)


__transonic__ = ('0.5.3',)
