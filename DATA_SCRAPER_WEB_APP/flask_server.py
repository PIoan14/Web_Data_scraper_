from flask import Flask , request, Response
from flask_cors import CORS
from check import check_message,make_df
from scrap import Net_to_CSV

app = Flask(__name__)
CORS(app, origins= "*")


@app.route('/')
def index():
    return 'Hello from the server'

@app.route('/send_message', methods=['POST', 'GET'])
def send_message():
    if request.method == 'POST':

        data = request.form
        data = dict(data)
        print(data)
        urls = check_message(data['message'])
        if len(urls) == 0 :
            def generate_fals():
                return 'No Data'

            response = Response(generate_fals(), mimetype='text/csv')
            response.headers.set("Content-Disposition", "attachment", filename="your_data.csv")
            return response
            #print('Gol.....de trimis un warning message')

        else:
            columns = [data['Company_name'], data['Email'], data['Phone_nr']]
            print(columns)
            data_frame = make_df(columns)
            print(type(data_frame))


            for url in urls:
                bot = Net_to_CSV(url)
                text_for_scrap = bot.scrap()
                aux = dict()
                for col in columns:

                    if col == 'Company Name':

                        name = bot.name_split()
                        aux.update({col : name})
                    elif col == 'Email':

                        email = bot.email_finder(text_for_scrap)
                        aux.update({col : email})
                    elif col == 'Phone number':
                        number = bot.phone_nr_finder(text_for_scrap)
                        aux.update({col : number})
                    else:
                        aux.update({col : ''})

                data_frame = data_frame._append(aux, ignore_index=True)

            csv_file_name = 'your_data.csv'
            data_frame.to_csv(csv_file_name)
            print(data_frame)

            def generate():
                with open(csv_file_name, 'r') as file:
                    yield from file.read()

            response = Response(generate(), mimetype='text/csv')
            response.headers.set("Content-Disposition", "attachment", filename="your_data.csv")
            return response

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')