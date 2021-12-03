from flask import Flask, render_template, request
from Schedule import Schedule
from WeeklyPay import WeeklyPay
from MonthlyPay import MonthlyPay
from Context import Context
import sqlite3 as sqlite

app = Flask(__name__, template_folder="Templates")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/newSchedule')
def new_schedule():
    return render_template('add_schedule.html')


@app.route('/updateSchedule')
def update():
    return render_template('update-schedule.html')


@app.route('/deleteSchedule')
def delete():
    return render_template('delete-schedule.html')


@app.route('/View_schedule', methods=['POST', 'GET'])
def get_schedule():
    try:

        advisor_name = request.form['Name']

        with sqlite.connect("Files/AdvisorScheduling.db") as con:

            print("Database opened successfully")

            cur = con.cursor()
            cur.execute("SELECT * FROM Schedule WHERE Advisor_Name LIKE '%" + advisor_name + "%'")
            rows = cur.fetchall()
            con.commit()
            msg = "Read Successfully"
            print(msg)

            # for row in rows:
            #   print("Advisor_Id:", row[0])
            #  print("Advisor_Name:", row[1])
            # print("Monday:", row[2])
            # print("Tuesday:", row[3])
            # print("Wednesday:", row[4])
            # print("Thursday:", row[5])
            # print("Friday:", row[6])
            # print("Total_Hours:", row[7])





    except:
        con.rollback()
        msg = "error while reading"


    finally:

        return render_template("index.html", rows=rows, msg=msg)
        con.close()


@app.route('/add_schedule', methods=['POST', 'GET'])
def add_schedule():
    msg = ""

    if request.method == 'POST':

        try:

            advisor_name = request.form['Advisor Name']
            total_hours = request.form['Total Hours']
            mon = request.form['mon']
            tue = request.form['tues']
            wed = request.form['wed']
            thur = request.form['thurs']
            fri = request.form['fri']

            schedule = Schedule()
            schedule.set_advisor_name(advisor_name)
            schedule.set_hours_per_week(total_hours)
            schedule.set_monday(mon)
            schedule.set_tuesday(tue)
            schedule.set_wednesday(wed)
            schedule.set_thursday(thur)
            schedule.set_friday(fri)

            # G0F Strategy pattern

            weekly = WeeklyPay()
            context = Context(weekly)
            weekly_pay = context.wage_computation(schedule)

            monthly = MonthlyPay()
            context = Context(monthly)
            monthly_pay = context.wage_computation(schedule)

            print("weekly pay for ", advisor_name, "will be", weekly_pay)

            print("monthly pay for ", advisor_name, "will be", monthly_pay)

            with sqlite.connect("Files/AdvisorScheduling.db") as con:

                print("Database opened successfully")

                cur = con.cursor()
                cur.execute("INSERT INTO Schedule(Advisor_Name, Monday, "
                            "Tuesday, Wednesday, Thursday, Friday, Total_hours)  VALUES(?,?,?,?,?,?,?)",
                            (advisor_name, mon, tue, wed, thur, fri, total_hours))

                con.commit()
                msg = "Added into schedule table Successfully"
                print(msg)

                cur = con.cursor()
                cur.execute("INSERT INTO Pay(Advisor_Name, Hours, "
                            "weekly_pay, Monthly_Pay)  VALUES(?,?,?,?)",
                            (advisor_name, total_hours, weekly_pay, monthly_pay))

                rows = cur.fetchall()
                con.commit()
                msg = "Added into Pay table Successfully"





        except:
            con.rollback()
            msg = "error while Adding"


        finally:

            return render_template("index.html", msg=msg)
            con.close()


@app.route('/update_schedule', methods=['POST', 'GET'])
def update_schedule():
    msg = ""
    if request.method == 'POST':

        try:
            advisor_name = request.form['Advisor Name']
            total_hours = request.form['Total Hours']
            mon = request.form['mon']
            tue = request.form['tues']
            wed = request.form['wed']
            thur = request.form['thurs']
            fri = request.form['fri']

            schedule = Schedule()
            schedule.set_advisor_name(advisor_name)
            schedule.set_hours_per_week(total_hours)
            schedule.set_monday(mon)
            schedule.set_tuesday(tue)
            schedule.set_wednesday(wed)
            schedule.set_thursday(thur)
            schedule.set_friday(fri)

            with sqlite.connect("Files/AdvisorScheduling.db") as con:

                print("Database opened successfully")

                cur = con.cursor()
                cur.execute(
                    "UPDATE Schedule SET Total_hours = ? , Monday = ?, Tuesday = ?, Wednesday = ?, "
                    "Thursday = ?, Friday = ?   WHERE Advisor_Name = ?",
                    (total_hours, mon, tue, wed, thur, fri, advisor_name))

                con.commit()
                msg = "Updated Successfully"
                print(msg)


        except:
            con.rollback()
            msg = "error while updating"


        finally:

            return render_template("index.html", msg=msg)
            con.close()


@app.route('/Delete_schedule', methods=['POST', 'GET'])
def delete_schedule():
    msg = ""
    if request.method == 'POST':

        try:
            schedule_id = request.form['Schedule Id']
            # schedule_id = int(schedule_id)

            print(schedule_id)

            with sqlite.connect("Files/AdvisorScheduling.db") as con:

                print("Database opened successfully")

                cur = con.cursor()
                cur.execute(
                    "DELETE FROM Schedule WHERE Schedule_Id =" + schedule_id + " ")
                con.commit()
                msg = "Deleted Successfully"
                print(msg)

        except:
            con.rollback()
            msg = "error while deleting"

        finally:

            return render_template("index.html", msg=msg)
            con.close()


if __name__ == "__main__":
    app.run()
