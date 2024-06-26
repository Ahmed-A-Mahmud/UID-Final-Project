from flask import Flask
from flask import render_template
from flask import Flask, request, redirect, url_for, render_template, jsonify
from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session  # You may need to install this with pip
import json
import random
import re

app = Flask(__name__)
app.config["SECRET_KEY"] = "ak4747"  # Necessary for session management
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

data = {
    1: {
        'lesson_id': 1,
        'word1': 'Mā',
        'word2': 'Māo',
        'word3': 'Tiān',
        'word4': 'Zhōu',
        'word1_trans': 'Mother',
        'word2_trans': 'Cat',
        'word3_trans': 'Sky',
        'word4_trans': 'Week',
        'imagelink1': 'https://lh3.googleusercontent.com/u/2/drive-viewer/AKGpihb0lIQuMNFHAuHiqss_uv58FY_ewNjiutFdHUTmWlUrYOdAmEpBLJKXL-wuZwApvN3uJqbn8Y2_2ixrMdGwkOMiQDQ14IK-Fg=w3456-h1984',
        'imagelink2': 'https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihZU2XYQkUdS-hDoiPjq7no7MoFOZSv6Xk3yQQWY0H2D2jhsrYTBTSyF6PfP1VmwFg69C5jJ3UISv_0Pxq5-Xdlwah00YlJ08Q=w1920-h878 ',
        'imagelink3': 'https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihYuqetuOiRbKobo99kwUmMhRghkFGqVsf-mRLCtxdFoEbpRk0M4VkhEIeteTyHkt2bCpCp4jy3bTQeevBXHfaHEzpNd12huzyk=w1920-h878 ',
        'imagelink4': 'https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihbtv7uJtaPx7Sz_wJolFjotTEb1CjUxSzCnKNHebgmingIy63HvzpCs-3vROzJQRVbOMNb1f0EfxwVQ8Q_s9G2nzcnrSUowfw=w1920-h878 ',
        'videolink1': 'https://player.vimeo.com/video/941498372?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479',
        'videolink2': 'https://player.vimeo.com/video/941498381?h=0d7a48351f"',
        'videolink3': 'https://player.vimeo.com/video/941498392?h=7226cbbf7d',
        'videolink4': 'https://player.vimeo.com/video/941498398?h=a60b42cb3b',
        'topOfPageText': 'You will begin by learning The Flat Tone. The flat tone means that through the vowel your voice will be at a consistently high and steady level. ',
        'topOfPageImage': 'https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihajeYRX1tUA9u9wC_btlakyDeKnHiwMQI8uG4XlbPD9GpWPXnuws18oihXIMoGwRQZNPd2VB7ZN_VQPkv1IoI70zaO-CIDdBQ=w2880-h1626-rw-v1 '
    },
    2: {
        'lesson_id': 2,
        'word1': 'Chá',
        'word2': 'Shí',
        'word3': 'Tí',
        'word4': 'Ná',
        'word1_trans': 'Tea',
        'word2_trans': 'Time',
        'word3_trans': 'Carry',
        'word4_trans': 'Take',
        'imagelink1': 'https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihZddB3wxpCFjY1vp2zT7nDvmcCmCzTdJkn66mUgqcJmcAwImgsG5_4meTuP-gCyPlV8fP-a_QM4c7owIXjvXE24D09J4JvgGr4=w1920-h878 ',
        'imagelink2': 'https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihbbOHni6d01KOoURB2cEIVQgc3_vmMaVFQ7SztIMabOqxus5ek7t-_Gsah2JE9ThYDSUgjLAGleHdf3aU7DE_msz2qBAUa1cR4=w1920-h878 ',
        'imagelink3': 'https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihagMFBJ55DP-xJoz3C4jHRc1LuRV8TGPk7pptXAmcmbLd8TPI_nrtvoJShu5SbgYD8RtMoVDOFn05Au_XA8d7waO-myGm4i7MM=w1920-h878-v0 ',
        'imagelink4': 'https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpiha20WGRT4N01gVeRHHhNiQ2KfY0jJhWoXZtPkgmFPcaiKqh0yxc4tqVmyIWzrN0dVPUOkevPVDGsd-P6r9CPs24KfxPeVtQbPk=w1920-h878-v0 ',
        'videolink1': 'https://player.vimeo.com/video/941498406?h=43e19a79ed',
        'videolink2': 'https://player.vimeo.com/video/941498414?h=2d9f29f6d1',
        'videolink3': 'https://player.vimeo.com/video/941498423?h=0b740646a4',
        'videolink4': 'https://player.vimeo.com/video/941498433?h=d59aeca992',
        'topOfPageText': 'The Rising tone means one has to make a clear rise in the word. Think of it as you’re asking a question! Or maybe when you’re asking “What?”',
        'topOfPageImage': 'https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihZfQs-DsrV8snnwTwIJvme9zR6jFzACdvgkkYRuZnQnRsGUK0yC_GioVb9qMAGAQ_z-q8vRiy4rklAaeBOz3Sfsc2mIV5c7Kg=w2880-h1626 '
    },
    3: {
        'lesson_id': 3,
        'word1': 'Wǒ',
        'word2': 'Mǎ',
        'word3': 'Cǎo',
        'word4': 'Dǎ',
        'word1_trans': 'Me',
        'word2_trans': 'Horse',
        'word3_trans': 'Grass',
        'word4_trans': 'Hit',
        'imagelink1': 'https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihYTpgwjcQ_IzGQpIwBnlbgwjZDQE0qeh3RyCIRxicqZeLSZYiISNZ21vCW04x6VGQ8l8xdFxwzEnBfan_KFhhwE5UG9pbleMNU=w1920-h878-v0 ',
        'imagelink2': 'https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihYx0vKgBjsbBd7L1XYp_W2Xe9xbGMKfGs3NhvY7CRcwBvU1gPrO8yfT02jjMVnq1tyjkyQgnHZH1_pApmUhwkE_9BbUIGgQCdY=w1920-h878 ',
        'imagelink3': 'https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihZ7Hb5-A3I_3nVHmA6QdlivJnV3uL2xqGWWJJiDIHnEDtRDGG2O4N_WjXykbFX8ryZU82Qxb_KCgyXPAmd3S8kfyhT3lwi9MA=w1920-h878-v0 ',
        'imagelink4': 'https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihZyTa4saKFH0eORNhtr3QVRZAh2aDZiW78LVWDJXo7x0akcyGhK5ZufqELsSJtKMh5PXI36sRlMMLaH3rOrzQ-i4Goq2g_Pqic=w1920-h878 ',
        'videolink1': 'https://player.vimeo.com/video/941498445?h=71193c3b10',
        'videolink2': 'https://player.vimeo.com/video/941498460?h=6ce177bdd9',
        'videolink3': 'https://player.vimeo.com/video/941498451?h=77d95db8f1',
        'videolink4': 'https://player.vimeo.com/video/941498468?h=4c7555ee55',
        'topOfPageText': 'The Dip tone is one where you have to begin by dipping, then raising it towards the end of the word. This one is tough to pronounce, but you’ll be able to spot it!',
        'topOfPageImage': 'https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpiha-TS1p1l012E5m7O8VKIYMOtI1itz2nr0-0Ya_Vx1IGwABzJFAtFKqc1JuqJHVSeRug-IwfYrBettQBln7bohRoR6QcPUS6Q=w2880-h1626'
    },
    4: {
        'lesson_id': 4,
        'word1': 'Duì',
        'word2': 'Kàn',
        'word3': 'Dào',
        'word4': 'Mà',
        'word1_trans': 'Correct',
        'word2_trans': 'Read',
        'word3_trans': 'Scold',
        'word4_trans': 'Go',
        'imagelink1': 'https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihYN72gAwnJCC3SrFUHYYaWdxNihYtHTnYlRBhcejuNp5CKIfcKzFIpSi_ti8eFpLbNUhKCrTKXfwY-KkruRs6AW9AUdX76z0A=w1920-h878 ',
        'imagelink2': 'https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihauI05XzkdK2aadYdwyKWjPLhT3_L3vMEGISaCNIJD8B5KEt9e23kuZ3Otk2cEdgeICTXbu8boP4vUswKZ5TPrNJCKcmMVExuY=w1920-h878 ',
        'imagelink3': 'https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihaXAtGku6eg9LZ3WUUjYS5vZpLyjCEIlCXZM0f7W3vO31ENOb1Os68vbAoU_AfciZ_7jCDmRoNVRiRxMrt8k8MYkOlzlEsnyrY=w1920-h878 ',
        'imagelink4': 'https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihZ0knOCtvi3UkyQj6_Oaf6rp_zEk1W1dUWYJT7UdbKpmlVoMaaXEWHxA_iEwPSFnxgclXRim-Rx7Dgz3OFXbdqE8V5xMUXJZw=w1920-h878 ',
        'videolink1': 'https://player.vimeo.com/video/941498475?h=332d0b3035',
        'videolink2': 'https://player.vimeo.com/video/941498484?h=8e6bbf46fe',
        'videolink3': 'https://player.vimeo.com/video/941498496?h=2ed71ab82d',
        'videolink4': 'https://player.vimeo.com/video/941498490?h=ff211a8975',
        'topOfPageText': 'The Descending tone is where the word starts high and quickly drops. One could think of it as rushing the word or saying the word in a “relaxed” manner.',
        'topOfPageImage': 'https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihakTl5m8T45673-MkK0mgnf6KDuHEqqFjSD8gaz6nlCXXaXuKdpv-ooPptdwPXXNEistDeSfnOTKifEhL08uEgSviAuwmzNRiE=w2880-h1626',
        'description': 'The fourth tone is where the word starts high and quickly drops. One could think of it as rushing the word or saying the word in a "relaxed" manner.'
    },
}

@app.route('/')
def index():
    session.clear()
    return render_template('index.html')

@app.route('/intro')
def intro():
    # For simplicity, just passing the raw data
    return render_template('intro.html')

@app.route('/learn/<int:lesson_id>')
def learn(lesson_id):
    myData = data.get(lesson_id)
    if not myData:  
        return "Page not found", 404
    
    # Determine the next lesson or transition to quiz intro
    tone_names = ["Flat Tone", "Rising Tone", "Dip Tone", "Descending Tone"]

    if lesson_id < 4:
        next_page = url_for('learn', lesson_id=lesson_id + 1)
        next_text = f"Move to {tone_names[lesson_id]}"  
    else:
        next_page = url_for('quiz_intro')
        next_text = "Begin Quiz"
    
    return render_template('learn.html', next_page=next_page, next_text=next_text, **myData)

@app.route('/quiz_intro')
def quiz_intro():
    # Initialize session variables needed for the quiz
    session['answered'] = []
    session['score'] = 0
    session['current_question'] = 1  # Make sure this is set before moving to quiz
    return render_template('quiz_intro.html')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    tone_titles = {
        'Tone 1': 'Flat Tone',
        'Tone 2': 'Rising Tone',
        'Tone 3': 'Dip Tone',
        'Tone 4': 'Descending Tone'
    }

    # Initialize session data if not present
    if 'answered' not in session:
        session['answered'] = []  # Tracks which tone-number and video-keys have been used
        session['current_question'] = 1  # Starts question numbering at 1
        session['score'] = 0  # Initialize score at 0

    if request.method == 'POST':
        choice = request.form.get('choice')
        correct_tone = session.get('current_correct_tone', 'Tone unavailable')

        # Map tone number to tone title
        correct_tone_title = tone_titles.get(correct_tone, 'Tone unavailable')

        if choice == correct_tone:
            feedback = 'Correct!'
            button_color = 'green'
            session['score'] += 1  # Increment score if the answer is correct
        else:
            feedback = f'Incorrect, the correct tone was {correct_tone_title}'
            button_color = 'red'

        # Check if it's the last question
        if session['current_question'] == 8:
            session['quiz_over'] = True
        else:
            session['current_question'] += 1  # Increment question number after submitting answer

        return jsonify({
            'feedback': feedback,
            'button_color': button_color,
            'correct_tone': correct_tone_title,
            'quiz_over': session.get('quiz_over', False)
        })

    # Load a new question or end the quiz
    if session.get('quiz_over', False):
        return redirect(url_for('results'))

    # Ensure unique tone and video pair for each question
    while True:
        tone_number = random.randint(1, 4)
        video_keys = ['videolink1', 'videolink2', 'videolink3', 'videolink4']
        random.shuffle(video_keys)  # Randomize video keys to select from

        for video_key in video_keys:
            if (tone_number, video_key) not in session['answered']:
                session['answered'].append((tone_number, video_key))
                video_url = data[tone_number][video_key]
                session['current_correct_tone'] = f'Tone {tone_number}'
                break
        else:
            continue
        break

    current_tone_title = tone_titles.get(session['current_correct_tone'], 'Tone unavailable')
    return render_template('quiz.html', video_url=video_url, correct_tone=current_tone_title, question_number=session['current_question'])

@app.route('/results')
def results():
    score = session.get('score', 0)
    return render_template('results.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)