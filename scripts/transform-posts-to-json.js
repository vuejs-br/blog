const {
  readFile,
  readdir,
  writeFile
} = require('fs')
const { promisify } = require('util')
const fm = require('front-matter')

const readFilePromise = promisify(readFile)
const readdirPromise = promisify(readdir)
const writeFilePromise = promisify(writeFile)

const buildPostName = (file, date) => {
  const postName = file
    .replace(`${date}-`, '')
    .replace('.md', '')
    .replace(/-/g, ' ')

  const [firstLetter, ...rest] = postName
  return `${firstLetter.toUpperCase()}${rest.join('')}`
}

async function run () {
  const PATH = `${process.cwd()}/posts`
  const filename = await readdirPromise(PATH)

  const posts = filename.map((file) => {
    const [date] = file.match(/(\d{4}-\d{2}-\d{2})/)
    const name = buildPostName(file, date)

    return {
      file,
      date,
      name
    }
  })

  const postsWithContent = await Promise.all(posts.map(async (post) => {
    const data = await readFilePromise(`${PATH}/${post.file}`, 'utf8')
    try {
      const content = fm(data)
      return {
        ...content,
        name: post.name,
        date: post.date
      }
    } catch (_) {
      return null
    }
  }))

  const postClean = postsWithContent.filter(post => Boolean(post))

  await writeFilePromise(`${process.cwd()}/tmp/posts.json`, JSON.stringify(postClean, null, 2))
  console.log('* Transform posts done!') // eslint-disable-line
}

run()
