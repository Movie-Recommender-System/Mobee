const HOST = 'http://localhost:8000/'

const ACCOUNTS = 'accounts/'
const ARTICLES = 'articles/'
const COMMENTS = 'comments/'
const MOVIES = 'movies/'
const REVIEWS = 'reviews/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
  },
  articles: {
    // /articles/
    articles: () => HOST + ARTICLES,
    // /articles/1/
    article: articlePk => HOST + ARTICLES + `${articlePk}/`,
    likeArticle: articlePk => HOST + ARTICLES + `${articlePk}/` + 'like/',
    comments: articlePk => HOST + ARTICLES + `${articlePk}/` + COMMENTS,
    comment: (articlePk, commentPk) =>
      HOST + ARTICLES + `${articlePk}/` + COMMENTS + `${commentPk}/`,
  },
  movies: {
    createMovies: () => HOST + MOVIES + 'create/',
    recentMovies: () => HOST + MOVIES + 'list/' + 'recent',
    wishedMovies: () => HOST + MOVIES + 'list/' + 'wish',
    recommendMovies: () => HOST + MOVIES +'recommendation/',
    movie: moviePK => HOST + MOVIES + `${moviePK}/`,
    reviews: moviePK => HOST + MOVIES + `${moviePK}/` + REVIEWS,
    review: (moviePK, reviewPK) => HOST + MOVIES + `${moviePK}/` + REVIEWS + `${reviewPK}/`,
  }
}
