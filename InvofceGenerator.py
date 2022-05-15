from flask import Flask, request, render_template, send_file
import os
import io 
from datetime import datetime
from weasyprint import HTML

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])

def f_api():
    posted_data = request.get_json()
    today = datetime.today().strftime("%B %-d, %Y")

    duadate = posted_data.get('duadate')
    from_addr = posted_data.get('from_addr')
    to_addr = posted_data.get('to_addr')
    invoice_number = posted_data.get('invoice_number')
    items = posted_data.get('items')

    total = sum([i['charge'] for i in items])
    rendered = render_template('invoice.html',
                             data = today,
                             from_addr = from_addr,
                             to_addr = to_addr,
                             items = items,
                             total = total,
                             invoice_number = invoice_number,
                             duedate = duadate     
    )
    html = HTML(string= rendered)
    render_pdf = html.write_pdf()
    return send_file(
        io.BytesIO(render_pdf),
        attachment_filename= 'invoice.pdf'
    )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
