import React, { Component } from 'react';
import axios from 'axios';

import classes from './ProfileFriends.module.css';
import ProfileFriendsItem from './ProfileFriendsItem/ProfileFriendsItem';

class ProfileFriends extends Component {

  state = {
    loading: true,
    friends: {}
  }

  componentDidMount() {
    let url = 'http://localhost:8000/api/friends/' + this.props.profile.id64
    axios.get(url)
      .then(res => {
        const friends = res.data;
        this.setState({friends})
        this.setState({loading: false})
      })
  }

  renderItems = () => {
    if(!this.state.loading) {
      let friends = this.state.friends.map((item, i) => {
        return <ProfileFriendsItem key={i} info={item}/>
      })
      return friends
    }
  }

  render() {
    console.log(this.state);
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