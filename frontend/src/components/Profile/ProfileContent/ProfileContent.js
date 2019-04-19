import React, { Component } from 'react';

import ProfileLastPlayed from './ProfileLastPlayed/ProfileLastPlayed';
import ProfileGamesOwned from './ProfileGamesOwned/ProfileGamesOwned';
import classes from './ProfileContent.module.css';

class ProfileContent extends Component {
  render() {
    console.log(this.props);
    return (
      <div className={classes.ProfileContent}>
        {this.props.profile.recent_games.total_count === 0 ? null : <ProfileLastPlayed recentGames={this.props.profile.recent_games}/>}
        <ProfileGamesOwned gamesOwned={this.props.profile.games_owned}/>
      </div>
    );
  }
}

export default ProfileContent;