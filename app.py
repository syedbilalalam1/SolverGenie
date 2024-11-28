from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'

@app.route('/')
def index():
    return render_template('index.html', page_title="Welcome to Maths Genie")

@app.route('/solve', methods=['POST'])
def solve():
    try:
        data = request.get_json()
        problem = data.get('problem')
        problem_type = data.get('type', 'math')

        if not problem:
            return jsonify({'error': 'No problem provided'}), 400

        return jsonify({
            'status': 'success',
            'problem': problem,
            'type': problem_type
        })

    except Exception as e:
        print(f"Error in /solve route: {e}")
        return jsonify({
            'error': 'An error occurred while processing the problem',
            'status': 'error'
        }), 500

@app.route('/word-problems')
def word_problems():
    return render_template('word_problems.html')

@app.route('/geometry-solver')
def geometry_solver():
    return render_template('geometry_solver.html')

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return redirect(url_for('index'))

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True) 