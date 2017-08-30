# Qiwi Wallet
# 15.07.2017
# Андрей Малых
from datetime_out import datetime_out
from random import randint
from random import choice

client_id = [5, 23, 91, 184, 206, 237, 250, 261, 354, 407]
client_debt = [234.5, 15.7, 9.43, 162.06, 21.5, 73.4, 43.3, 54.12, 42.4, 0.0]
	
# Функция для оплаты
def pay():
	prove_2 = False
	while prove_2 != True:
		try:
			v_id = int(input("\n\t\tВведите номер счета: "))
		except ValueError:
			print("Вы ввели не правильные данные.")
		else:
			prove_2 = True
	prove_2 = False
	for x in range(0,10):
		if v_id < client_id[x]:
			prove = False;
			break
		if v_id == client_id[x]:
			sd = client_debt[x] # Переменная sd - для сохранение баланса клиента
			prove = True
			break
	if prove == True:
		print("\n\n\t\tНа вашем счете: ", sd, "$")
		print("\n\tЧто вы хотели бы оплатить? \n")
		print("\tПожертвование - 10$")
		print("\tТЕЛЕ2 - 3.75$")
		print("\tМТС - 3.75")
		print("\tSteam - 59.99$")
		v_pay = str(input("\t\t\t"))
		if v_pay == "Пожертвование":
			if sd >= 10:
				print("\t\tДата: " + datetime_out())
				print("\n\n\t\tОплата успешно произведена!")			
			else:
					print("\n\n\t\tНедостаточно средств!")
		elif v_pay == "ТЕЛЕ2":
			if sd >= 3.75:
				print("\t\tДата: " + datetime_out())
				print("\n\n\t\tОплата успешно произведена!")
			else:
					print("\n\n\t\tНедостаточно средств!")
		elif v_pay == "МТС":
			if sd >= 3.75:
				print("\t\tДата: " + datetime_out())
				print("\n\n\t\tОплата успешно произведена!")       
			else:
					print("\n\n\t\tНедостаточно средств!")
		elif v_pay == "Steam":
			if sd >= 59.99:
				print("\t\tДата: " + datetime_out())
				print("\n\n\t\tОплата успешно произведена!")
			else:
					print("\n\n\t\tНедостаточно средств!")
		else:
			print("\n\n\t\tОплата недоступна!")
	else:
		print("\n\n\t\tТакого счета не существует!")    

# Функция для пополнения
def add():
	commis = 0.05
	ac = 0.0
	ad = 0.0
	prove_2 = False
	while prove_2 != True:
		try:
			v_id = int(input("\n\t\tВведите номер счета: "))
		except ValueError:
			print("Вы ввели не правильные данные.")
		else:
			prove_2 = True
	prove_2 = False
	for x in range(0,10):
		if v_id < client_id[x]:
			prove = False;
			break
		if v_id == client_id[x]:
			sd = client_debt[x]
			prove = True
			break
	if prove == True:
		print("\n\n\t\tНа вашем счете: ", sd, "$")
		print("\n\n\t\tПополнение счета.")
		print("\n\tКомиссия:")
		print("\t0-10$    -5%")
		print("\t >10$    -0%")
		while prove_2 != True:
			try:
				ac = float(input("\t\tВнесите средства: "))
			except ValueError:
				print("Вы ввели неправильные данные.")
			else:
				prove_2 = True
		if ac > 10:
			ad = ac
			commis = 0
		else:
			ad = ac - ac * commis
			commis = ac - ad 
		print("\n\t\tПринято: ", ac)
		print("\t\tЗачислено: ", ad)
		print("\t\tКомиссия: " + " %.2f" % (commis))
		print("\t\tДата: " + datetime_out())
		print("\n\n\t\tПополнение успешно произведено!")	
	else:
		print("\n\n\t\tТакого счета не существует!")    


# Главное меню  
print("\t\t\tQiwi Кошелек")
print("\tОплатить\t\t\tПополнить")
print("\t\t\t Выход")
while 1 == 1:
	vbr = str(input("\t\t\t"))
	if vbr == "Оплатить":
		pay()
		break

	if vbr == "Пополнить":
		add()
		break
	if vbr == "Выход":
		break
