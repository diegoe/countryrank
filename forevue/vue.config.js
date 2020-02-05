module.exports = {
    publicPath: '/static/backcountry/',
    outputDir: '../backcountry/static/backcountry/',
    devServer: {
        proxy: 'http://127.0.0.1:8000'
    },
}
