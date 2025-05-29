from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv("dataset.csv")  # replace with your CSV file

    preview = df.head().to_html(classes='table table-bordered table-striped', index=False)

    import io
    buffer = io.StringIO()
    df.info(buf=buffer)
    df_info = buffer.getvalue()

    # Top 10 cuisines
    top_cuisines = df['Cuisines'].value_counts().head(10).to_dict()

    # Table Booking status
    table_booking_status = df['Has Table booking'].value_counts().to_dict()

    return render_template('index.html',
                           preview=preview,
                           df_info=df_info,
                           top_cuisines=top_cuisines,
                           table_booking_status=table_booking_status)

if __name__ == '__main__':
    app.run(debug=True)
