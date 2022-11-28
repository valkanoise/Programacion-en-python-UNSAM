# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
mes = 1


#mientras haya deuda el while es TRUE
while saldo > 0:
    
#condicional para hacer pagos extra entre los meses 61 y 108
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra
        print(mes, round(total_pagado,2), round(saldo,2))
        mes = mes + 1
        
        
# pago para la ultima cuota cuando el saldo es menos a la cuota mensual, se modifica la cuota para saldar la deduda y dejar saldo = 0      
# este condiciona solo se ejecuta en la ultima cuota
    elif saldo <= pago_mensual:
        pago_mensual = saldo * (1+tasa/12) # modifico el pago mensual para que sea el saldo del mes anterior mas los intereses del mes corriente
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
        print(mes, round(total_pagado,2), round(saldo,2))
        mes = mes + 1

#pagos normales fuera de los meses de pago extra      
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
        print(mes, round(total_pagado,2), round(saldo,2))
        mes = mes + 1
        
        
        
print('Total pagado', round(total_pagado, 2))
print("Meses: ", mes-1)