def calcular_puntajes(diplomados, especialidades, maestrias, doctorados):
    subtotal = 0
    puntajes = [0, 0, 0, 0]  # [Diplomados, Especialidad, Maestría, Doctorado]
    
    # Jerarquía: Doctorado -> Maestría -> Especialidad -> Diplomado
    # Doctorado
    doctorado_p = min(12 * doctorados, 12)
    add = min(doctorado_p, 12 - subtotal)
    puntajes[3] = add
    subtotal += add
    
    if subtotal < 12:
        # Maestría
        if maestrias <= 0:
            maestria_p = 0
        else:
            maestria_p = min(8 + 3*(maestrias - 1), 11)
        add = min(maestria_p, 12 - subtotal)
        puntajes[2] = add
        subtotal += add
        
        if subtotal < 12:
            # Especialidad
            if especialidades <= 0:
                especialidad_p = 0
            else:
                especialidad_p = min(4 + 2*(especialidades - 1), 6)
            add = min(especialidad_p, 12 - subtotal)
            puntajes[1] = add
            subtotal += add
            
            if subtotal < 12:
                # Diplomado
                if diplomados <= 0:
                    diplomado_p = 0
                else:
                    diplomado_p = min(2 + 1*(diplomados - 1), 4)
                add = min(diplomado_p, 12 - subtotal)
                puntajes[0] = add
                subtotal += add
    
    return (
        puntajes[0],  # Diplomado
        puntajes[1],  # Especialidad
        puntajes[2],  # Maestría
        puntajes[3],  # Doctorado
        min(subtotal, 12)  # Subtotal
    )

