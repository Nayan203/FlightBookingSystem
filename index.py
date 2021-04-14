# from DB_Connect import *
import random
import mysql.connector as db

class Flight(object):

    def getBusinessSeat(self):
        con = db.connect(user='root', password='', host='localhost', database='flightbookingsystem')
        cursor = con.cursor()
        print('Press 1 for Window Seat else 2 for Aisle Seat.')
        choice = int(input('Enter the number: '))
        if choice == 1:
            query = '''Select SeatNo, Category, Status from  businessclass where Category = 'Window' and Status = 'Unreserved' '''
            cursor.execute(query)
            allseat = cursor.fetchall()
            for seat in allseat:
                print(seat)
            print('\nDo you want to book your seat?')
            print('Press 1 for booking')
            progress = int(input('enter the Number: '))
            if progress == 1:
                PassengerName = input('\nEnter the Passenger Name: ')
                PassengerEmail = input('Enter the Passenger Email: ')
                Booking_ID = random.randint(10000, 20000)
                SeatNo = input('Enter the Seat No. of your choice: ')
                query = '''update businessclass set Status = 'Reserved', BookingID = %s, PName = %s, 
                PEmail = %s WHERE SeatNo = %s '''
                d1 = (Booking_ID, PassengerName, PassengerEmail, SeatNo)
                cursor.execute(query, d1)
                con.commit()
                print('Thanks for choosing us', PassengerName, 'your ticket has been booked.')
                print(PassengerName, 'your Seat No. is:', SeatNo)
                print(PassengerName, 'your Booking ID is:', Booking_ID)
                con.close()
            else:
                print('Thanks for visiting us.')

        elif choice == 2:
            query = '''Select SeatNo, Category, Status from  businessclass where Category = 'Aisle' and Status = 'Unreserved' '''
            cursor.execute(query)
            allseat = cursor.fetchall()
            for seat in allseat:
                print(seat)
            print('\nDo you want to book your seat?')
            print('Press 1 for booking')
            progress = int(input('enter the Number: '))
            if progress == 1:
                PassengerName = input('\nEnter the Passenger Name: ')
                PassengerEmail = input('Enter the Passenger Email: ')
                Booking_ID = random.randint(10000, 20000)
                SeatNo = input('Enter the Seat No. of your choice: ')
                query = '''update businessclass set Status = 'Reserved', BookingID = %s, PName = %s, 
                            PEmail = %s WHERE SeatNo = %s '''
                d1 = (Booking_ID, PassengerName, PassengerEmail, SeatNo)
                cursor.execute(query, d1)
                con.commit()
                print('Thanks for choosing us', PassengerName, 'your ticket has been booked.')
                print(PassengerName, 'your Seat No. is:', SeatNo)
                print(PassengerName, 'your Booking ID is:', Booking_ID)
                con.close()
            else:
                print('Thanks for visiting us.')

        else:
            print('Wrong Input. Try Again....!')
# ------------------------------------------------------------------------------------------------------------

    def getEconomySeat(self):
        con = db.connect(user='root', password='', host='localhost', database='flightbookingsystem')
        cursor = con.cursor()
        print('Press 1 for Window Seat or 2 for Middle Seat 0r 3 for Aisle Seat.')
        choice = int(input('Enter the number: '))
        if choice == 1:
            query = '''Select SeatNo, Category, Status from  economyclass where Category = 'Window' 
                    and Status = 'Unreserved' '''
            cursor.execute(query)
            allseat = cursor.fetchall()
            for seat in allseat:
                print(seat)
            print('\nDo you want to book your seat?')
            print('Press 1 for booking')
            progress = int(input('enter the Number: '))
            if progress == 1:
                PassengerName = input('\nEnter the Passenger Name: ')
                PassengerEmail = input('Enter the Passenger Email: ')
                Booking_ID = random.randint(10000, 20000)
                SeatNo = input('Enter the Seat No. of your choice: ')
                query = '''update economyclass set Status = 'Reserved', BookingID = %s, PName = %s, 
                PEmail = %s WHERE SeatNo = %s '''
                d1 = (Booking_ID, PassengerName, PassengerEmail, SeatNo)
                cursor.execute(query, d1)
                con.commit()
                print('Thanks for choosing us', PassengerName, 'your ticket has been booked.')
                print(PassengerName, 'your Seat No. is:', SeatNo)
                print(PassengerName, 'your Booking ID is:', Booking_ID)
                con.close()
            else:
                print('Thanks for visiting us.')

        elif choice == 2:
            query = '''Select SeatNo, Category, Status from  economyclass where Category = 'Middle' and Status = 'Unreserved' '''
            cursor.execute(query)
            allseat = cursor.fetchall()
            for seat in allseat:
                print(seat)
            print('\nDo you want to book your seat?')
            print('Press 1 for booking')
            progress = int(input('enter the Number: '))
            if progress == 1:
                PassengerName = input('\nEnter the Passenger Name: ')
                PassengerEmail = input('Enter the Passenger Email: ')
                Booking_ID = random.randint(10000, 20000)
                SeatNo = input('Enter the Seat No. of your choice: ')
                query = '''update economyclass set Status = 'Reserved', BookingID = %s, PName = %s, 
                            PEmail = %s WHERE SeatNo = %s '''
                d1 = (Booking_ID, PassengerName, PassengerEmail, SeatNo)
                cursor.execute(query, d1)
                con.commit()
                print('Thanks for choosing us', PassengerName, 'your ticket has been booked.')
                print(PassengerName, 'your Seat No. is:', SeatNo)
                print(PassengerName, 'your Booking ID is:', Booking_ID)
                con.close()

        elif choice == 3:
            query = '''Select SeatNo, Category, Status from  economyclass where Category = 'Aisle' and Status = 'Unreserved' '''
            cursor.execute(query)
            allseat = cursor.fetchall()
            for seat in allseat:
                print(seat)
            print('\nDo you want to book your seat?')
            print('Press 1 for booking')
            progress = int(input('enter the Number: '))
            if progress == 1:
                PassengerName = input('\nEnter the Passenger Name: ')
                PassengerEmail = input('Enter the Passenger Email: ')
                Booking_ID = random.randint(10000, 20000)
                SeatNo = input('Enter the Seat No. of your choice: ')
                query = '''update economyclass set Status = 'Reserved', BookingID = %s, PName = %s, 
                            PEmail = %s WHERE SeatNo = %s '''
                d1 = (Booking_ID, PassengerName, PassengerEmail, SeatNo)
                cursor.execute(query, d1)
                con.commit()
                print('Thanks for choosing us', PassengerName, 'your ticket has been booked.')
                print(PassengerName, 'your Seat No. is:', SeatNo)
                print(PassengerName, 'your Booking ID is:', Booking_ID)
                con.close()
            else:
                print('Thanks for visiting us.')

        else:
            print('Wrong Input. Try Again....!')

# ---------------------------------------------------------------------------------------------------
    def getBookingDetails(self):
        con = db.connect(user='root', password='', host='localhost', database='flightbookingsystem')
        cursor = con.cursor()
        print('press 1 if you have booked in Business Class else 2 if you booked in Economy Class')
        check = int(input('Enter your choice: '))
        if check == 1:
            pname = input('Enter Passengers Name: ')
            query = ''' select * from businessclass where PName = '%s' '''
            cursor.execute(query% pname)
            detail = cursor.fetchall()
            if len(detail) > 0:
                print('Passenger Name is:', detail[0][5])
                print('Passenger Seat No. is:', detail[0][1])
                print('Passenger Booking ID is:', detail[0][4])
                print('Passenger Email ID is:', detail[0][6])
                con.close()
            else:
                print('No data is found with this name.')
            
            
        elif check == 2:
            pname = input('Enter Passengers Name: ')
            query = '''select * from economyclass where PName = '%s' '''
            cursor.execute(query% pname)
            detail = cursor.fetchall()
            if len(detail) > 0:
                print('Passenger Name is:', detail[0][5])
                print('Passenger Seat No. is:', detail[0][1])
                print('Passenger Booking ID is:', detail[0][4])
                print('Passenger Email ID is:', detail[0][6])
                con.close()
            else:
                print('No data is found with this name.')
              
        else:
            print('Entered Wrong choice... Try Again!!')

# -----------------------------------------------------------------------------------------------------
    def cancelBooking(self):
        con = db.connect(user='root', password='', host='localhost', database='flightbookingsystem')
        cursor = con.cursor()
        print('\nEnter 1 if you have booked in Business Class else 2 if you booked in Economy Class')
        check = int(input('Enter your choice: '))
        if check == 1:
            passenger_name = input('Enter the Passenger Name: ')
            query = '''select PName,SeatNo from businessclass where PName = '%s' '''
            cursor.execute(query% passenger_name)
            detail = cursor.fetchall()
            if len(detail) > 0:
                pname = detail[0][0]
                pseatno = detail[0][1]
                query = '''update businessclass set Status = 'Unreserved', BookingID = '', PName = '',
                            PEmail = '' WHERE SeatNo = '%s' '''
                cursor.execute(query % pseatno)
                con.commit
                print(passenger_name, 'your booking has been cancelled.')
                con.close
            else:
                print('No data is found.')


        elif check == 2:
            passenger_name = input('Enter the Passenger Name: ')
            query = '''select PName,SeatNo from economyclass where PName = '%s' '''
            cursor.execute(query % passenger_name)
            detail = cursor.fetchall()
            if len(detail) > 0:
                pname = detail[0][0]
                pseatno = detail[0][1]
                query = '''update economyclass set Status = 'Unreserved', BookingID = NULL, PName = '',
                                        PEmail = '' WHERE SeatNo = '%s' '''
                cursor.execute(query % pseatno)
                con.commit
                print(passenger_name, 'your booking has been cancelled.')
                con.close
            else:
                print('No data is found.')

# ------------------------------------------------------------------------------------------------------

f1 = Flight()

print('\n*************  Welcome To Bhopal Airlines  *************\n')

print('Enter 1 to book Business Seat')
print('Enter 2 to book Economy Seat')
print('Enter 3 to get Booking Details')
print('Enter 4 to cancel the  ticket\n')
choice = int(input('Enter your choice: '))
if choice == 1:
    f1.getBusinessSeat()
elif choice == 2:
    f1.getEconomySeat()
elif choice == 3:
    f1.getBookingDetails()
elif choice == 4:
    f1.cancelBooking()
else:
    print('Entered Wrong Choice. Try Again!!')


