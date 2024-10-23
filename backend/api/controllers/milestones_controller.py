@app.route('/projects/<int:project_id>/milestones', methods=['POST'])
def add_milestone(project_id):
    data = request.json
    milestone_id = add_milestone(project_id, data['description'])
    return jsonify({"milestone_id": milestone_id}), 201

@app.route('/projects/<int:project_id>/milestones/<int:milestone_id>/complete', methods=['POST'])
def complete_milestone(project_id, milestone_id):
    complete_milestone(project_id, milestone_id)
    return jsonify({"status": "success"}), 200
