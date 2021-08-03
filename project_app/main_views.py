from flask import Blueprint, render_template, request
from sqlalchemy import func
from datetime import datetime
from werkzeug.utils import redirect
from project_app.models import db
from project_app.models import Post

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    post_list = Post.query.order_by(Post.create_date.desc())
    return render_template('index.html',post_list = post_list)


@main_bp.route('/post_write', methods=["GET","POST"])
def post_write():
    if request.method == "POST":
        post = Post(subject=request.form['subject'], content=request.form['contents'], create_date=datetime.now())
        db.session.add(post)
        db.session.commit()
        return redirect('http://localhost:5000/')#redirect(url_for('/'))
    else:
        return render_template('post_write.html')

@main_bp.route('/post_view/<int:id>')
def post_view(id):
    post = Post.query.filter(Post.id==id).first()
    return render_template('post_view.html',post=post)


@main_bp.route('/post_modify/<int:id>', methods=['GET','POST'])
def post_modify(id):
    if request.method == 'GET':
        post = Post.query.filter(Post.id==id).first()
        return render_template('post_modify.html', post=post)
    else:
        post = Post.query.filter(Post.id==id).first()
        post.subject = request.form['subject']
        post.content = request.form['contents']
        db.session.commit()
        return redirect('/post_view/'+ str(id))