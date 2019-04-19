import React, { Component } from 'react';

import classes from './ProfileLastPlayedItem.module.css'

class ProfileLastPlayedItem extends Component {

  playtimeTwoWeeks = () => {
    let hours = Math.floor(this.props.game.playtime_2weeks / 60);
    let mins = this.props.game.playtime_2weeks % 60;

    if(hours === 0) {
      return `${mins} minutes`
    }
    else {
      return `${hours} hours and ${mins} minutes`
    }

  }

  render() {
    console.log(this.props);
    return (
      <div className={classes.ProfileLastPlayedItem}>
        <div className={classes.ProfileLastPlayedImage}>
          <img src={`https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/${this.props.game.appid}/${this.props.game.img_logo_url}.jpg`} alt="game_logo"/>
        </div>
        <div className={classes.ProfileLastPlayedInfo}>
          <span className={classes.GameTitle}>{this.props.game.name}</span>
        </div>
        <div className={classes.ProfileLastPlayedTime}>
          <div>{this.playtimeTwoWeeks()} logged in 2 weeks</div>
          <div>{Math.floor(this.props.game.playtime_forever / 60)} total hours played</div>
        </div>
      </div>
    );
  }
}

export default ProfileLastPlayedItem;