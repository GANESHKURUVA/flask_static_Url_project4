from flask import Flask,render_template


FAI=Flask(__name__)


@FAI.route('/ganesh')
def ganesh():
    return render_template('ganesh.html')



@FAI.route('/dhoniimg')
def dhoni():
    return render_template('dhoni.html')



if __name__=='__main__':
    FAI.run(debug=True)