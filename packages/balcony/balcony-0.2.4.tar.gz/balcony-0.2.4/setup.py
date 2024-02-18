# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['balcony', 'balcony.custom_nodes', 'balcony.terraform_import']

package_data = \
{'': ['*'], 'balcony': ['custom_tf_import_configs/*', 'custom_yamls/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'PyYAML>=6.0,<7.0',
 'boto3>=1.24.80,<2.0.0',
 'inflect>=6.0.0,<7.0.0',
 'jmespath>=1.0.1,<2.0.0',
 'mkdocs-autorefs>=0.4.1,<0.5.0',
 'mkdocs-material>=8.5.7,<10.0.0',
 'mkdocstrings[python]>=0.21.2,<0.22.0',
 'pydantic>=1.10.7,<2.0.0',
 'rich>=13.3.4,<14.0.0',
 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['balcony = balcony.cli:run_app']}

setup_kwargs = {
    'name': 'balcony',
    'version': '0.2.4',
    'description': 'Read any resource in your AWS Account. You can generate terraform code for them, too.',
    'long_description': '# balcony\n\n\n<div style="display: flex;">\n  <a href="https://github.com/oguzhan-yilmaz/balcony/actions/workflows/docker-publish.yml"><img src="https://github.com/oguzhan-yilmaz/balcony/actions/workflows/docker-publish.yml/badge.svg" alt="Build and publish a Docker image to ghcr.io"></a>\n  <span style="width: 5px"></span>\n\n<a href="https://github.com/oguzhan-yilmaz/balcony/actions/workflows/pages/pages-build-deployment"><img src="https://github.com/oguzhan-yilmaz/balcony/actions/workflows/pages/pages-build-deployment/badge.svg" alt="Build and Deploy Documentation website"></a>\n</div>\n\n\nbalcony is a modern CLI tool that with some killer features:\n\n- Auto-fill the required parameters for AWS API calls \n- Read the JSON data of any AWS resource in your account\n- Generate [Terraform Import Blocks](https://developer.hashicorp.com/terraform/language/import)\n- Generate actual `.tf` Terraform Resource code\n\nbalcony uses _read-only_ operations, it does not take any action on the used AWS account.\n\n\n### [Visit the Documentation Website](https://oguzhan-yilmaz.github.io/balcony/quickstart/)\n<!-- ### [**Go to QuickStart Page to get started using _balcony_**](quickstart.md) -->\n\n### Installation\n\n```bash\npip3 install balcony\n```\n\nVisit [**Installation & QuickStart Page**](https://oguzhan-yilmaz.github.io/balcony/quickstart/) to get started using _balcony_\n\n```bash  title="Basic usage"\n# see options\nbalcony\n\n# list available resources of ec2\nbalcony aws ec2 \n\n# read a resource\nbalcony aws s3 Buckets\n\n# show documentation\nbalcony aws iam Policy --list\n\n# generate terraform import blocks for a resource\nbalcony terraform-import s3 Buckets\n```\n\n\n## Features\n\n### Read any AWS Resource\n\n`balcony aws <service> <resource-name> --paginate` command reads all resources of a given type in your AWS account.\n\nRelated Docs: [QuickStart](https://oguzhan-yilmaz.github.io/balcony/quickstart/)\n\n![](https://raw.githubusercontent.com/oguzhan-yilmaz/balcony-assets/main/gifs/aws-read-resource.gif)\n\n\n---\n\n### Generate Terraform Import Blocks\n\nTerraform v1.5 introduced [import blocks](https://developer.hashicorp.com/terraform/language/import) that allows users to define their imports as code.\n\n`balcony terraform-import <service> <resource-name>` command generates these import blocks for you.\n\n`balcony terraform-import --list` to see the list of supported resources.\n\nRelated Docs: [Generate Terraform Import Blocks](https://oguzhan-yilmaz.github.io/balcony/terraform-import/)\nRelated Docs: [Balcony Terraform Import Support Matrix](https://oguzhan-yilmaz.github.io/balcony/terraform-import-support-matrix/)\n\n\n\n![](https://raw.githubusercontent.com/oguzhan-yilmaz/balcony-assets/main/gifs/terraform-import-blocks-example.gif)\n\n\n---\n\n### Generate actual Terraform Resource Code \n\n\nIf you have:\n\n- initialized terraform project\n- `import_blocks.tf` file that\'s generated with `balcony terraform-import` command\n\nyou can run `terraform plan -generate-config-out=generated.tf` to generate actual `.tf` resource code.\n\nThis feature is achieved with the [balcony-terraform-import Docker Image](https://github.com/oguzhan-yilmaz/balcony/pkgs/container/balcony-terraform-import).\n\n\nRelated Docs: [Generate Terraform Code with Docker Image](https://oguzhan-yilmaz.github.io/balcony/terraform-import-docker/)\n\n![](https://raw.githubusercontent.com/oguzhan-yilmaz/balcony-assets/main/gifs/docker-gen-tf-code-ec2-insances-example.gif)\n\n\n---\n\n### Interactive Wizard to create balcony import configurations \n\nBalcony doesn\'t know how to create terraform `import blocks` for all of the AWS resources.\n\nIt can be taught how to do it by creating `import-configurations` yaml files, but it\'s a manual process. This is where the interactive wizard comes in.\n\nInteractive Wizards asks you required questions to automatically create the `import-configurations` yaml files.\n\nRelated Docs: [Terraform Import Configuration Wizard](https://oguzhan-yilmaz.github.io/balcony/terraform-import-wizard/)\n\n![](https://raw.githubusercontent.com/oguzhan-yilmaz/balcony-assets/main/gifs/terraform-wizard-security-groups-example.gif)\n',
    'author': 'Oguzhan Yilmaz',
    'author_email': 'oguzhanylmz271@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
