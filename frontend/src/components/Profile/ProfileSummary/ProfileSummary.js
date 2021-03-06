import React, { Component } from 'react'

import classes from './ProfileSummary.module.css';

import ProfileSummaryBadges from './ProfileSummaryBadges/ProfileSummaryBadges';

export default class ProfileSummary extends Component {

  render() {
    console.log(this.props);
    return (
      <div className={classes.ProfileSummary}>
        <div className={classes.ProfilePicture}>
            <img src={this.props.profile.avatar_full} alt="Profile"/>
        </div>
        <div className={classes.ProfileNameSection}>
          <span className={classes.ProfileName}>{this.props.profile.name}</span>
          <a href={this.props.profile.steam_url}>Visit Steam Profile</a>
        </div>
        <div className={classes.ProfileLevel}>
          <span>Level {this.props.profile.badges.player_level}</span>
          <span>Total xp: {this.props.profile.badges.player_xp} | Next level: {this.props.profile.badges.player_xp_needed_to_level_up}</span>
          <ProfileSummaryBadges id64={this.props.profile.id64} badges={this.props.profile.badges.badges}/>
        </div>
      </div>
    )
  }
}
