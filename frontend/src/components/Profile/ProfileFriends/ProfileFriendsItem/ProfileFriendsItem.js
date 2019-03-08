import React, { Component } from 'react';

import classes from './ProfileFriendsItem.module.css';

class ProfileFriendsItem extends Component {

  render() {
    return (
      <div className={classes.ProfileFriendsItem}>
        <div className={classes.ProfileFriendsItemImage}>
          <img src={this.props.info.avatar_med} alt="friend pic"/>
        </div>
        <div className={classes.ProfileFriendsItemInfo}>
          <span className={classes.Name}>{this.props.info.name}</span>
          <span className={classes.OnlineStatus}>Online</span>
          <span>{this.props.info.id64}</span>
        </div>
      </div>
    );
  }
}

export default ProfileFriendsItem;