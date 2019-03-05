import React, { Component } from 'react';

import classes from './ProfileFriendsItem.module.css';

class ProfileFriendsItem extends Component {

  render() {
    console.log(this.props.info);
    return (
      <div className={classes.ProfileFriendsItem}>
        <img src="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/cc/cce5172c7699199761f3f7b8185fc8d33fa9bcff_medium.jpg" alt="friend pic"/>
        <div>
          <span className={classes.Name}>SUPER COOL BEASLEY BOY SEFES ESF ES FESF </span>
          <span className={classes.OnlineStatus}>Online</span>
          <span>{this.props.info.steamid}</span>
        </div>
      </div>
    );
  }
}

export default ProfileFriendsItem;