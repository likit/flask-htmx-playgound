from flask import render_template, jsonify

from app.datatable import table_bp


@table_bp.route('sweetalert')
def show_info_sweetalert():
    return render_template('datatable/info-display-sweetalert.html')


@table_bp.route('api/demo/item/<int:dataid>')
def get_data_info(dataid):
    data = [
        {
            'id': 1,
            'title': 'One',
            'message': 'Item 1'
        },
        {
            'id': 2,
            'title': 'Two',
            'message': 'Item 2'
        },
        {
            'id': 3,
            'title': 'Three',
            'message': 'Item 3'
        },
    ]
    for item in data:
        if item['id'] == dataid:
            return jsonify(item)
    return jsonify({})