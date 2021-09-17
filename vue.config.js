module.exports = {
    publicPath: '/carstore/',
    configureWebpack: {
        externals: {
            'AMap': 'AMap',
            'AMapUI': 'AMapUI'
        }
    },
}