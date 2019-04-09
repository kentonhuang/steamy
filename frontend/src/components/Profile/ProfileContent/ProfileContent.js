import React, { Component } from 'react';

import ProfileLastPlayed from './ProfileLastPlayed/ProfileLastPlayed';
import ProfileGamesOwned from './ProfileGamesOwned/ProfileGamesOwned';
import classes from './ProfileContent.module.css';

class ProfileContent extends Component {
  render() {
    console.log(this.props);
    return (
      <div className={classes.ProfileContent}>
        <ProfileLastPlayed recentGames={this.props.profile.recent_games}/>
        <ProfileGamesOwned />
      </div>
    );
  }
}

export default ProfileContent;