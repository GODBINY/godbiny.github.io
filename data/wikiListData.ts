interface wikiList {
  title: string
  description: string
  href?: string
  imgSrc?: string
}

const wikiListData: wikiList[] = [
  {
    title: 'コーディングテストでよく使われる関数',
    description: `基本的な関数だけど時々思いつかないこと`,
    href: 'https://godbiny.github.io/blog/wikiData/Wiki-%E9%96%A2%E6%95%B0',
  },
  {
    title: 'ギット',
    description: `ギット`,
    href: 'https://www.google.com',
  },
]

export default wikiListData
