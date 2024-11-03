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
    imgSrc: '/static/images/prepare.avif',
    href: 'https://www.google.com',
  },
  {
    title: 'ギット',
    description: `ギット`,
    imgSrc: '/static/images/prepare.avif',
    href: 'https://www.google.com',
  },
]

export default wikiListData
