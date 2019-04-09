import React, { Component } from 'react';

import ProfileLastPlayedItem from './ProfileLastPlayedItem';
import classes from './ProfileLastPlayed.module.css'

class ProfileLastPlayed extends Component {

  mapRecentlyPlayed = () => {
    let games = this.props.recentGames.games.map((game, i) => {
      return <ProfileLastPlayedItem game={game} key={i} />
    })
    return games;
  }

  render() {
    console.log(this.props);
    return (
      <div className={classes.ProfileLastPlayed}> 
        {this.mapRecentlyPlayed()}
      </div>
    );
  }
}

export default ProfileLastPlayed;