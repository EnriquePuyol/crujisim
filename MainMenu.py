#!/usr/bin/python
#-*- coding:iso8859-15 -*-

# (c) 2005 CrujiMaster (crujisim@yahoo.com)
#
# This file is part of CrujiSim.
#
# CrujiSim is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# CrujiSim is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CrujiSim; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA


import banner
import Metepasadas
import tpv

[accion, fir_elegido , sector_elegido , ejercicio_elegido , imprimir_fichas] = banner.seleccion_usuario()

# accion = "ejecutar", "modificar", "nueva"

print "Returned tuple:", [accion, fir_elegido , sector_elegido , ejercicio_elegido , imprimir_fichas]

if accion == "modificar":
	Metepasadas.modificar([fir_elegido , sector_elegido , ejercicio_elegido , imprimir_fichas])
elif accion == "nueva":
	Metepasadas.nueva()
elif accion == "ejecutar":
	tpv.set_seleccion_usuario([fir_elegido , sector_elegido , ejercicio_elegido , imprimir_fichas])
	import Simulador
