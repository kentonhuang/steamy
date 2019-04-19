import React, { Component } from 'react';
import axios from 'axios'

import classes from './ProfileGamesOwned.module.css';
import ProfileGameItem from './ProfileGameItem';

class ProfileGamesOwned extends Component {

  state = {
    loading: true,
    games: {}
  }

  componentDidMount() {
    let games = this.props.gamesOwned.games.map((game) => {
      return game.appid;
    })
    let gamesStr = games.join(',');
    let url = 'http://localhost:8000/api/game/?id=' + gamesStr
    let result = this.getUrl(url);
    axios.get(url)
      .then(res => {
        let arr = [];
        let urls = [];
        const games = res.data;
        arr.push(...games.results)
        if(games.count > 20) {
          let ceil = Math.ceil(games.count / 20);
          for(let i = 2; i <= ceil; i++) {
            urls.push(url + `&page=${i}`)
          }
        }
        if(urls.length === 0) {
          this.setState({games})
          this.setState({loading: false})
        }
        return {
          arr,
          urls
        }
      })
      .then(res => {
        console.log(res);
      })
      
    // let promiseArr = urls.map(link => 'hey');
    // console.log(promiseArr);
    // axios.all(promiseArr)
    // .then(res => {
    //   console.log('hey');
    // }) 
    // console.log(result);
  }

  async getUrl(url) {
    let data = await axios.get(url)
    return data;
  }

  mapGames = () => {
    let games = this.props.gamesOwned.games.map((game, i) => {
      return <ProfileGameItem game={game} key={i} />
    })
    return games;
  }

  render() {
    console.log(this.state);
    return (
      <div className={classes.ProfileGamesOwned}>
        {this.mapGames()}
      </div>
    );
  }
}

export default ProfileGamesOwned;