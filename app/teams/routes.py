from flask import render_template, url_for, flash, redirect, request, Blueprint
from app.teams.logic import Teams
from app.utils.util import TeamAbbreviations

teams = Blueprint('teams', __name__)


@teams.route('/teams/<team_name>/home', methods=['GET'])
def team_home(team_name):
    team_text, image = TeamAbbreviations.team_info.get(team_name.upper())
    title = TeamAbbreviations.team_mapping.get(team_name.upper())
    image_file = url_for('static', filename=image)

    return render_template('account.html', title=title, image_file=image_file, body=team_text)


@teams.route('/teams/<team_name>/matches', methods=['GET'])
def matches(team_name):
    team = TeamAbbreviations.team_mapping.get(team_name.upper())
    team_obj = Teams(team)
    team_stats = team_obj.matches_info_per_team()
    return render_template('about.html', matches=team_stats['Matches'], won=team_stats['Won'], lost=team_stats['Lost'],
                           tied=team_stats['Tie'], nr=team_stats['NR'])

