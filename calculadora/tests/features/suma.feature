Feature: Suma de dos numeros
	yo como usuario de la app calculadora 
	quiero relizar  una suma de dos numeros 
	para poder tener un resultado confiable.



	Scenario: Sumar 2 más 2
		dado que tengo los operadores "2" y "2"
		cuando realizo la suma 
		entonces el resultado que obtengo es "4"

	Scenario: Restar 2 menos 1
		dado que tengo los operadores "2" y "1"
		cuando realizo la resta 
		entonces el resultado que obtengo es "1"

	Scenario: Multiplicacion 5 menos 5
		dado que tengo los operadores "5" y "5"
		cuando realizo la multiplicacion 
		entonces el resultado que obtengo es "25"

	Scenario: Divicion 100 menos 5
		dado que tengo los operadores "100" y "5"
		cuando realizo la divicion
		entonces el resultado que obtengo es "20"


