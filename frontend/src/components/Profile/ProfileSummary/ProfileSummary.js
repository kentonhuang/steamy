import React, { Component } from 'react'

import classes from './ProfileSummary.module.css';

export default class ProfileSummary extends Component {
  render() {
    return (
      <div className={classes.ProfileSummary}>
        <div className={classes.ProfilePicture}>
            <img src={this.props.profile.avatar_full} alt="Profile"/>
        </div>
      </div>
    )
  }
}
