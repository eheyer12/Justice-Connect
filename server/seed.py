from app import app
from models import db, Client, Lawyer, Lawfirm, Case

with app.app_context():
    print("🗑 Clearing db...")
    Client.query.delete()
    Lawyer.query.delete()
    Lawfirm.query.delete()
    Case.query.delete()

    print('👨‍💼 Seeding clients...')
    clients = []
    clients.append(Client(username="eheyer12", role="labor"))
    clients.append(Client(username="unicoroni", role="tax"))
    clients.append(Client(username="brave782", role="family"))

    # db.session.add_all(clients)

    print('⚖️ Seeding lawyers...')
    lawyers = []
    lawyers.append(Lawyer(title="Seventh Year", lawfirm_id=1))
    lawyers.append(Lawyer(title="Third Year", lawfirm_id=3))
    lawyers.append(Lawyer(title="First Year", lawfirm_id=2))

    # db.session.add_all(lawyers)

    print('🏛️ Seeding lawfirms...')
    lawfirms = []
    lawfirms.append(Lawfirm(title="Cravath LLP", rank=1))
    lawfirms.append(Lawfirm(title="Davis Polk LLP", rank=2))
    lawfirms.append(Lawfirm(title="Skadden", rank=3))

    # db.session.add_all(lawfirms)

    print('📂 Seeding cases...')
    cases = []
    cases.append(Case(title="Employment", body="A labor law case.", client_id=1, lawyer_id=1))
    cases.append(Case(title="Fraud", body="A tax law case.", client_id=2, lawyer_id=3))
    cases.append(Case(title="Divorce", body="A family law case.", client_id=3, lawyer_id=2))
    
    db.session.add_all(clients)
    db.session.add_all(lawyers)
    db.session.add_all(lawfirms)
    db.session.add_all(cases)
    db.session.commit()
    print("🌱Done Seeding!🌱")