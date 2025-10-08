def clasificar(densidades):
    return list(map(lambda d: "Liviana" if d < 2.5 else "Media" if d <= 7.0 else "Pesada", densidades))