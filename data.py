import requests

url = 'http://127.0.0:5000/'

data = {
        'duadate' : 'May 15, 2022',
        'from_addr' : { 
            'addr_1' : 'El jadida, Morocco',
            'addr_2' : 'lot 4',
            'school_name' : "ecole des siences de l'information"
        },
        'invoice_number' : 145,
        'items' : [{
            'charge' : 500,
            'title' : 'app web',

        },
        {
            'charge' : 600,
            'title' : 'hosting',

        },
        {
            'charge' : 500,
            'title' : 'app mobile',

        }
        ],
        'to_addr' : {
            'company_name' : 'esi.me',
            'person_email' : 'salah@exemple.ma',
            'person_name' : 'salaheddin sanad'
        }
}

html = requests.post(url,json=data)
with open('invoice.pdf','wb') as f :
    f.write(html.content)

