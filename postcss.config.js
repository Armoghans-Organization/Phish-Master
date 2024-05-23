module.exports = {
  plugins: [
    require('@fullhuman/postcss-purgecss')({
      content: [
        './app/templates/**/*.html',
        './app/static/**/*.js',
      ],
      defaultExtractor: content => content.match(/[\w-/:]+(?<!:)/g) || []
    })
  ]
}
