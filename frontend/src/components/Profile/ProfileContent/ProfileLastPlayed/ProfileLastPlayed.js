import React, { Component } from 'react';

import ProfileLastPlayedItem from './ProfileLastPlayedItem';
import classes from './ProfileLastPlayed.module.css'

class ProfileLastPlayed extends Component {
  render() {
    return (
      <div class={classes.ProfileLastPlayed}> 
        <ProfileLastPlayedItem />
        <ProfileLastPlayedItem />
        <ProfileLastPlayedItem />
        <ProfileLastPlayedItem />
      </div>
    );
  }
}

export default ProfileLastPlayed;