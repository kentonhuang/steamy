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
        let promiseArr = res.urls.map(link => axios.get(link))
        let arr = res.arr;
        axios.all(promiseArr).then(res => {
          for(let i = 0; i < res.length; i++) {
            arr.push(...res[i].data.results)
          }
          console.log(arr);
          this.setState({games: arr})
          this.setState({loading: false})
        })
      })
  }

  mapGames = () => {
    if (!this.state.loading) {
      let games = this.state.games.map((game, i) => {
        const found = this.props.gamesOwned.games.find(ele => ele.appid === game.id);
        return <ProfileGameItem game={game} key={i} info={found}/>
      })
      return games;
    }
  }

  render() {
    return (
      <div className={classes.ProfileGamesOwned}>
        {this.mapGames()}
      </div>
    );
  }
}

export default ProfileGamesOwned;