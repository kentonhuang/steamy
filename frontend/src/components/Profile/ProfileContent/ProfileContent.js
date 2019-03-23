import React, { Component } from 'react';

import ProfileLastPlayed from './ProfileLastPlayed/ProfileLastPlayed';
import classes from './ProfileContent.module.css';

class ProfileContent extends Component {
  render() {
    return (
      <div className={classes.ProfileContent}>
        <ProfileLastPlayed />
      </div>
    );
  }
}

export default ProfileContent;