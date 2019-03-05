import React, { Component } from 'react';

import classes from './ProfileFriends.module.css';
import ProfileFriendsItem from './ProfileFriendsItem/ProfileFriendsItem';

class ProfileFriends extends Component {

  renderItems = () => {
    let friends = this.props.profile.friends.friends.map((item, i) => {
      return <ProfileFriendsItem key={i} info={item}/>
    })
    return friends;
  }

  render() {
    console.log(this.props);
    return (
      <div className={classes.ProfileFriends}>
        <span>FRIENDS</span>
        <div className={classes.FriendsList}>
          {this.renderItems()}
        </div>
        <div className={classes.coverBar}></div>
      </div>
    );
  }
}

export default ProfileFriends;