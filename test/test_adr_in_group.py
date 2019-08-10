

def test_adr_in_group(app):
    app.addline.first_adr_fist_group()

def test_adr_in_specgroup(app):
    app.addline.first_adr_spec_group(app)

def test_alladr_in_specgroup(app):
    app.addline.alladr_in_specgroup(app)
