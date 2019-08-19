<template>
  <div>
    <h2>Twitcasting Live分析</h2>
    <input type="text" v-model="userid" placeholder="ユーザーID" class="form-control">
    <button type="button" class="btn btn-primary" v-on:click="getUserInfo()">表示</button>

    <table class="table">
      <thead>
        <tr>
          <th scope="col">タイトル</th>
          <th scope="col">開始</th>
          <th scope="col">配信時間</th>
          <th scope="col">合計視聴者数</th>
          <th scope="col">最大視聴者数</th>
          <th scope="col">コメント数</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(movie, idx) in info" :key="idx">
          <td>{{ movie.title }}</td>
          <td>{{ movie.created }}</td>
          <td>{{ movie.duration }}</td>
          <td>{{ movie.total_view_count }}</td>
          <td>{{ movie.max_view_count }}</td>
          <td>{{ movie.comment_count }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      info: null,
      userid: null
    };
  },
  methods: {
    getUserInfo() {
        axios.get(
          "http://localhost:5000/userinfo/"+this.userid
        ).then(response => {
          this.info = response.data.movies
        })
    }
  },
  created () {
    this.getUserInfo()
  }
}
</script>
