from app import app, process_data

if __name__ == '__main__':
    process_data()
    app.run(debug=False, host='0.0.0.0')
