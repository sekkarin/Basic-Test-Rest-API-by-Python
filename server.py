from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample data
posts = [
    {"id": 1, "title": "First Post", "content": "This is the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the second post."}
]

# Function to find a post by ID
def find_post(post_id):
    return next((post for post in posts if post["id"] == post_id), None)

# CREATE a new post
@app.route('/posts', methods=['POST'])
def create_post():
    if not request.json or not 'title' in request.json:
        abort(400, "Title is required.")
    new_post = {
        "id": posts[-1]["id"] + 1 if posts else 1,
        "title": request.json["title"],
        "content": request.json.get("content", "")
    }
    posts.append(new_post)
    return jsonify(new_post), 201

# READ all posts
@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

# READ a specific post
@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = find_post(post_id)
    if post is None:
        abort(404, "Post not found.")
    return jsonify(post)

# UPDATE a specific post
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = find_post(post_id)
    if post is None:
        abort(404, "Post not found.")
    if not request.json:
        abort(400, "Request body is required.")
    if 'title' in request.json and not isinstance(request.json['title'], str):
        abort(400, "Title must be a string.")
    if 'content' in request.json and not isinstance(request.json['content'], str):
        abort(400, "Content must be a string.")
    post["title"] = request.json.get("title", post["title"])
    post["content"] = request.json.get("content", post["content"])
    return jsonify(post)

# DELETE a specific post
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = find_post(post_id)
    if post is None:
        abort(404, "Post not found.")
    posts.remove(post)
    return jsonify({"message": "Post deleted successfully."})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
