import React, { Component } from 'react';

class ProfileGameItem extends Component {
  render() {
    console.log(this.props);
    return (
      <div>
        {this.props.game.name}
      </div>
    );
  }
}

export default ProfileGameItem;