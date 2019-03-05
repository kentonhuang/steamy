import React, { Component } from 'react'
import { withRouter } from 'react-router-dom'

import ProfileSummary from '../components/Profile/ProfileSummary/ProfileSummary';
import ProfileContent from '../components/Profile/ProfileContent/ProfileContent';
import ProfileFriends from '../components/Profile/ProfileFriends/ProfileFriends';

class ProfilePage extends Component {
  render() {
      console.log(this.props.location);
    return (
      <React.Fragment>
        <ProfileSummary profile={this.props.location.state.profile}/>
        <ProfileContent profile={this.props.location.state.profile}/>
        <ProfileFriends profile={this.props.location.state.profile}/>
      </React.Fragment>
    )
  }
}

export default withRouter(ProfilePage);