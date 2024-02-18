from email.message import EmailMessage
import ssl
import smtplib

email_emisor = 'macruzgraphic@gmail.com'
email_contrasena = 'ctge kegf jpht bush'
email_receptor = 'sparkyxd1234@gmail.com'

asunto = 'Texto de ejemplo prueba 1'
cuerpo = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed 
    do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Aliquam vestibulum morbi blandit cursus. Nisl condimentum id venenatis 
    a condimentum vitae sapien pellentesque habitant. Erat pellentesque adipiscing 
    commodo elit at imperdiet dui accumsan sit. Adipiscing diam donec adipiscing tristique. 
    Tellus rutrum tellus pellentesque eu tincidunt tortor. Nulla facilisi morbi tempus iaculis 
    urna id. Enim ut sem viverra aliquet. Nisl tincidunt eget nullam non nisi 
    est sit amet facilisis. Tincidunt eget nullam non nisi est sit. Enim praesent 
    elementum facilisis leo vel fringilla est ullamcorper eget. Morbi tempus iaculis 
    urna id volutpat lacus laoreet non curabitur. Egestas pretium aenean pharetra magna 
    ac placerat. Adipiscing enim eu turpis egestas pretium. Sagittis eu volutpat odio 
    facilisis. Nulla facilisi morbi tempus iaculis urna id volutpat lacus. 
    Et sollicitudin ac orci phasellus egestas tellus rutrum tellus pellentesque. 
    Duis at consectetur lorem donec massa sapien. Velit aliquet sagittis id 
    consectetur purus ut. Vel risus commodo viverra maecenas accumsan lacus vel facilisis.

"""

em = EmailMessage()
em['From'] = email_emisor
em['To'] = email_receptor
em['Subject'] = asunto
em.set_content(cuerpo)


#Scurity

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
    smtp.login(email_emisor, email_contrasena)
    smtp.sendmail(email_emisor, email_receptor, em.as_string())